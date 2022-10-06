# Video Scale Changer
  <p align="center">
    <i>
The purpose of this project is to create a service using the Django framework that receives the video files and with the FFmpeg service, converts and saves this files for low quality such as 480 and 360. When the original video was uploaded in Video model, Celery service find it and placed it in the queue, then converted it to other qualities and stored it again in the same Django model.
     
    NOTIC : This solution focused on back-end and it has been implemented in the admin panel.
  </p>
 
  <hr>
 
</p>


<h3>
⭐️ Tools used  
</h3>

<ul>
  <li>
    Used Django as base framework 
  </li>
  <li>
    Used Postgres for backend databse
  </li>
  <li>
    Used Pytest for write effective unit test
  </li>
  <li>
    Used FFmpeg service for video edit
  </li>
  <li>
    Used FFmpeg service for video edit
  </li>
  <li>
    Used Celery task queue with redis backend
  </li>
</ul>
<hr>

  <p>
  The Django framework is used in this project, because it provides a powerful admin panel that is one of Django's built-in features for starting work and implementing features, and this project is also implemented in the Django management panel.
  </p>


<hr>

### Thanks to..
* [Django](https://djangoproject.com)

###### Made with :heart:
