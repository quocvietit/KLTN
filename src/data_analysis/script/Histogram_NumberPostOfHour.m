%read file data
file = fileread('./../../data/bbcnews_posts_2014_07042018.json');

%load to json
json_data = jsondecode(file);

%show data
json_data

% Create figure
figure1 = figure;

% Create axes
axes1 = axes('Parent',figure1);
hold(axes1,'on');

%custom histogram
nbins = 20;
edges_min = min([json_data.created_time_hour]) - 0.5;
edges_max = max([json_data.created_time_hour]) + 0.5;

edges = [edges_min edges_max];
hist = histogram([json_data.created_time_hour]);
xlim(axes1, edges);

%show histogram 
hist
