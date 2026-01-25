import spatialdata as sd
from napari_spatialdata import Interactive

# Read in the remote object
# points not yet working, so no transcripts :(
sdata = sd.read_zarr("https://radosgw.public.os.wwu.de/omics-data/VISUALIZATION/ZARR2-MB299-ALIGNED.zarr/", selection=("images", "labels", "tables"))

# Prepare the napari viewer 
interactive = Interactive(sdata)
# Launch the viewer
interactive.run()

