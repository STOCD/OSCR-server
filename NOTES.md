# NOTES

django-OSCR intends to be a REST-only API built on top of Django and
Django Rest Framework. The goal here is to create a microservice which can
provide a backend to OSCR-related GUIs and Web Services. Existing examples of
these are as follows:

GUIs:
- SCM
- CLR

Web Services: 
- [STO DPS webtools](http://sto-dps.danfai.de/)

# Apps
## user
This is for managing the superuser right now with the intent of adding user
support in the future (feature request: sets integration). The superuser gets
access to Django's admin dashboard as that's likey all we really need for a
management interface for now.

## combatlog
This is for managing combat logs and will provide APIs to do the following:
    - Upload a Combat Log for analysis
    - Download Stored Combat Logs
    - Viewing Combat Log metadata (Using OSCR as a backend)

Where the Combat Log model is defined as:
    - A metadata model which describes the combat log.
    - A the actual combat log data (for auditing purposes, or to regenerate
      metadata if OSCR changes its parsing algorithm).

## ladder
This is for managing ladders. The goal is to have ladders managed by a fixture
for easy creation of new ladders depending on community feedback. The API would
allow at minimum:
    - The ability to fetch ladder results for a given ladder.
    - The ability to provide rich filtering (likely using django_filter) to
      easily analyze Character / handle / ladder data.

Ideally there would be two models here.
    - A ladder model which represents a map/difficulty (e.g. ISE, Solo ISE)
    - A ladder results model which is a foreign key to a ladder which contains a
      combat log and its metadata.

Having an individual ladder results model/view allows for querying by various
fields (e.g.):

### Scenario 1 (Looking for my results on ISE):
    - Map: ISE
    - Handle: @sdkraust

### Scenario 2 (Looking for all my @handle's results):
    - Handle: @sdkraust

### Scenario 3 (Looking for my exact character's results):
    - Player: Kraust@sdkraust

### Scenario 4 (Access to DPS Prime):
    - Map: ISA or ISE or HSE
    - DPS >= 500k

The individual ladders need to reference the map output by OSCR so its ultimately
limited by what OSCR can detect.


# Secrity / Tampering Concerns

Originally, there will be no authentication for log uploading but uploaded logs
need to pass any of OSCR's map detection checks. However, Django was used because
of its rich security middleware, and like all web servers can be placed in front
of a proxy like nginx for additional security. Some middleware I'm familiar with
that address the security side include:

- [Django Axes](https://github.com/jazzband/django-axes) - Login auditing and lockout.
- [Django Oauth Toolkit](https://github.com/jazzband/django-oauth-toolkit) - OAuth Integration with Django.


(If you haven't figured it out yet, I am a fan of jazzband's Django middleware)

Ultimately there is not much to "attack" here except to pollute the db with bad
data. I'm not sure if that's currently a risk factor with SCM, CAT and CLR and if
it ever becomes one, the best possible solution is to create a user registration
system and provide API keys to individual users for use with the API consumers
(this is trivial to implement with django).


# API Clients

- [drf-yasg](https://github.com/axnsan12/drf-yasg) - I am a huge proponent of
OpenAPI and have used it for over half of a decade. This will allow anyone to
easily integrate with this project.
