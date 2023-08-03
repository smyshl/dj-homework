# def test_example():
#     assert False, "Just test example"
import pytest
from model_bakery import baker
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student():
    return Student.objects.create(name='Петр Петров')


@pytest.fixture
def course():
    return Course.objects.create(name='Математика')


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_course_retrieve(client, course_factory):
    # Arrange
    course_factory(_quantity=10)
    first_course_id = Course.objects.first().id
    url = reverse('courses-detail', kwargs={'pk': first_course_id})

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == Course.objects.get(id=first_course_id).name


@pytest.mark.django_db
def test_course_list(client, course_factory):
    # Arrange
    course_factory(_quantity=10)
    url = reverse('courses-list')

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == Course.objects.count()


@pytest.mark.django_db
def test_course_id_filter(client, course_factory):
    # Arrange
    course_factory(_quantity=10)
    first_course_id = Course.objects.first().id
    url = reverse('courses-list')

    # Act
    response = client.get(url, {'id': first_course_id})

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['id'] == first_course_id


@pytest.mark.django_db
def test_course_name_filter(client, course_factory):
    # Arrange
    course_factory(_quantity=7)
    check_name = False
    name_count = 0
    for i in range(3):
        Course.objects.create(name='Физика')
        name_count += 1
    url = reverse('courses-list')

    # Act
    response = client.get(url, {'name': 'Физика'})

    # Assert
    assert response.status_code == 200
    data = response.json()
    for row in data:
        if row['name'] == 'Физика':
            check_name = True
    assert check_name
    assert len(data) == name_count

@pytest.mark.django_db
def test_course_create(client):
    count = Course.objects.count()
    url = reverse('courses-list')
    data = {'name': 'Физика'}

    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.json()['name'] == 'Физика'
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_course_update(client, course_factory):
    course_factory(_quantity=10)
    first_course_id = Course.objects.first().id
    first_course_name = Course.objects.get(id=first_course_id).name
    url = reverse('courses-detail', kwargs={'pk': first_course_id})

    response = client.put(url, {'name': 'Физика'})
    new_course_name = Course.objects.get(id=first_course_id).name

    assert response.status_code == 200
    assert response.json()['name'] == new_course_name
    assert first_course_name != new_course_name


@pytest.mark.django_db
def test_course_delete(client, course_factory):
    course_factory(_quantity=10)
    first_course_id = Course.objects.first().id
    course_count = Course.objects.all().count()
    url = reverse('courses-detail', kwargs={'pk': first_course_id})

    response = client.delete(url)

    assert response.status_code == 204
    assert not Course.objects.filter(id=first_course_id)
    assert Course.objects.all().count() == course_count - 1

