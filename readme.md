## Setup Environment (for Ubuntu)

1. Download Meshroom release binaries from [https://github.com/alicevision/Meshroom/releases/tag/v2023.1.0](https://github.com/alicevision/Meshroom/releases/tag/v2023.1.0)
2. Extract the tarball.
3. Set the RELEASE_ROOT var in `set_env_vars.sh` to point to the extracted directory.
4. Clone Meshroom source code `git clone --recursive --branch v2023.1.0 https://github.com/alicevision/meshroom`
5. Set the MESHROOM_ROOT var in `set_env_vars.sh` to point to the cloned repo. 


```
source set_env_vars.sh
```

## Meshroom reconstruction pipeline

Run pipeline:

```
python meshroom_batch --input imgs/ --pipeline meshroom_pipeline.mg  --output batch_output -v trace  --save computed_graph.mg
```



## Blender

U need to have Blender installed in your OS, that can be run from command line like: `blender`.
Run the following command to load the reconstructed scene to blender and filter 'background' vertices, leaving solely 
the Jack Daniels bottle (and a small fragment of the chair the bottle was placed upon).
bottle 
```
blender --python blender_select_vertices_to_cut.py
```
