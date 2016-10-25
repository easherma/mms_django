# init structure


## models
### user
user may submit to any maps they are a member of(or access from a specific permalink?)

row_id
user_id
user_name
user_email
story_id
path_order
geom(point)
notes


###
story ~ groups of maps?

story_id
story_name
story_description
story_instructions


###
maps ~ geojson?

not sure if this is a model or a route...basically thinking we'd run the query to group users by a requested story and parse that output to send JSON(geoJSON ideally) to the frontend
