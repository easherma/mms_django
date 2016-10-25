# init structure


## models
### user
user may submit to any maps they are a member of(or access from a specific permalink?)

```
row_id
user_id
user_name
user_email
story_id
path_order
geom(point)
notes
```


### story
```
story_id
story_name
story_description
story_instructions
```

### maps (groups of users by story as geojson?)

not sure if this is a model or a route...basically thinking we'd run the query to group users by a requested story and parse that output to send JSON(geoJSON ideally) to the frontend

### views
* general:
  * homepage: shows a random submission
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
