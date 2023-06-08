#!/bin/bash

export MESHROOM_ROOT=../meshroom
export PYTHONPATH=$MESHROOM_ROOT:$PYTHONPATH

# using existing alicevision release

RELEASE_ROOT=/home/bartlomiej/studia/mgr/twm/Meshroom-2023.1.0-av3.0.0-centos7-cuda11.3.1

export LD_LIBRARY_PATH=$RELEASE_ROOT/aliceVision/lib/
export PATH=$PATH:$RELEASE_ROOT/aliceVision/bin/
export QT_PLUGIN_PATH=$RELEASE_ROOT/qtPlugins
export QML2_IMPORT_PATH=$RELEASE_ROOT/qtPlugins/qml
export ALICEVISION_ROOT=$RELEASE_ROOT/aliceVision
export ALICEVISION_SENSOR_DB=$RELEASE_ROOT/aliceVision/share/aliceVision/cameraSensors.db
export ALICEVISION_VOCTREE=$RELEASE_ROOT/aliceVision/share/aliceVision/vlfeat_K80L3.SIFT.tree
