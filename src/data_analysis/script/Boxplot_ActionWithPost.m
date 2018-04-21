%read file data
file = fileread('./../../data/bbcnews_posts_2014_07042018.json');

%load to json
json_data = jsondecode(file);

%show data
json_data