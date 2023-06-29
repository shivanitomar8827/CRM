{% for user in users %}
  <tr>
    <td><a href="{% url 'user_note_create' user.username %}">{{ user.first_name }}</a></td>
    <td>{{ user.last_name }}</td>
    <td>{{ user.email }}</td>
  </tr>
from django.urls import path
from . import views



urlpatterns = [
    # Other URL patterns
    path('user_note_create/<str:username>/', views.user_note_create, name='user_note_create'),
    # Other URL patterns
]
<tbody>
  {% for user in users %}
  <tr onclick="redirectToUserNoteCreate('{{ user.username }}')" style="cursor: pointer;">
    <td>{{ user.first_name }}</td>
    <td>{{ user.last_name }}</td>
    <td>{{ user.email }}</td>
  </tr>
  {% endfor %}
</tbody>
</table>

<script type="text/javascript">
function redirectToUserNoteCreate(username) {
  var url = "{% url 'user_note_create' '_username' %}".replace('username_', username);
  window.location.href = url;
}
</script>