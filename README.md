# Offline visual-inertial 3D reconstruction

Sample data for debugging can be found [here](https://yadi.sk/d/5fo291FEG9yAAg).

You need to install this plugin into blender: https://github.com/uhlik/bpy (save this file: https://raw.githubusercontent.com/uhlik/bpy/master/space_view3d_point_cloud_visualizer.py)

* Install and activate addon in a usual way.
* Add any object type to scene.
* Go to 3d View Sidebar (N) > Point Cloud Visualizer tab, click file browser icon, select ply file, click Load PLY. Reload button next to it reloads ply from disk.
* Click Draw button to display point cloud, Erase to hide point cloud. Adjust percentage of displayed points with Display, point size with Size and point transparency with Alpha.
* Display point normals as lines - click Normal icon, adjust line length with Length next to it.
* Transforming parent object transforms point cloud as well.
* Illumination ‘adds’ single artificial light on points, you can edit its direction and strength. Works only when vertex normals are present.
* When vertex colors are missing, cloud will be displayed in uniform gray, in that case you can enable Illumination to have better cloud view
