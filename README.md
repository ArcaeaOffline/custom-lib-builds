# OpenCV Custom Android Builds

Slimmed-down OpenCV 5.x Android AAR with Java bindings, built on GitHub Actions.

## Modules

`core, flann, geometry, imgproc, imgcodecs, dnn, java`

Everything else (features, objdetect, photo, video, videoio, highgui, stitching,
calib, stereo, ptcloud, ts) is excluded. The OpenCV source tree is **never
modified** — customisation is done via:

- `configs/opencv.config.py` — ABI list, consumed by `build_sdk.py --config`
- `.github/workflows/build.yml` — module list, NDK pin, environment handling

## How to run

1. **Build (artifact only)**: GitHub → Actions → *Build OpenCV Android AAR* →
   *Run workflow* → leave `opencv_version` as-is, keep `release` unchecked.
   Artifacts (`*.aar` + maven repo) expire after 90 days.
2. **Publish (GitHub Release)**: same as above but check `release`. A release
   tagged `5.0.0` (same as the OpenCV version) is created/overwritten with the
   AAR and the maven repository attached.

Republishing the same OpenCV version replaces the existing release (the tag is
deleted and recreated at the current default-branch HEAD).

The AAR is the **shared-library build** (`libopencv_java5.so` per ABI, full
Java bindings in `classes.jar`) — drop-in compatible with the official
`org.opencv:opencv` artifact consumed via `OpenCVLoader.initLocal()`.
The generated `maven_repo` uses the same coordinates (`org.opencv:opencv`),
so consumers only need to point a local maven repo at it.

## Version pinning

- OpenCV source: shallow-cloned from the official repo at the given git tag;
  the resolved commit SHA is recorded in the workflow run summary.
- GitHub Actions: pinned by full commit SHA (with `# vX.Y.Z` comments),
  updated automatically via Dependabot.
- Android NDK: pinned to `27.3.13750724`; AGP 8.6 builds with SDK CMake 3.31.x
  (the bundled CMake 4.x is removed from the runner's SDK before building).

## Expected build time

~1.5–2.5 h on a standard 4-core runner (4 ABIs, TBB/IPP/KleidiCV enabled).
