from django.urls import path
from .views import create_list_audio, get_update_audio,delete_audio


urlpatterns = [
    # create and get list of audiotypefile url
    path("<str:audioFileType>/list-audio-create/", create_list_audio),

    # get and update perticular audiofiletype url
    path("<audioFileType>/<int:pk>/", get_update_audio),

    # delete perticular audiofiletype url
    path("delete/<audioFileType>/<int:pk>/", delete_audio),

]
