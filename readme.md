# init structure


## models


### story

```
story_name
story_description
story_instructions
```

### user
user may submit to any maps they are a member of(or access from a specific permalink?)

```
story_id(FK)
user_name
user_email
```
### waypoint
```
geom(point)
notes
path_order
```

### submissions

```
user_id
story_id
waypoint_id
```




### views
* general:
  * homepage: shows a specific submission
  * story page: permalink for a single story
  * gallery of stories: lists created stories

* stories:
  * prompts: form for making a story
  * results: permalink for created story

* user
  * prompts: form for submitting user submission
  * results: permalink for user submission
  * story: see all submissions for the story you submitted to (switch between these?)

* maps
  * still not sure if this is relevant or how this fits in to the above model (thinking about how I need to pass stuff to leaflet)
