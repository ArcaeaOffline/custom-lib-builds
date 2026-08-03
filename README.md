# Custom Android Builds

Custom builds of OpenCV and ONNX Runtime for Android, produced by GitHub
Actions. The upstream sources are never modified; everything is configured
through `configs/` and the workflow files.

## Artifacts

| Artifact | Maven coordinates |
|---|---|
| OpenCV AAR (shared lib, full Java bindings) | `org.opencv:opencv:5.0.0` |
| ONNX Runtime AAR (reduced ops, see `configs/ort/ops.config`) | `com.microsoft.onnxruntime:onnxruntime-android:1.26.0` |

Both keep the official coordinates, so consumers override the official
artifacts through a local maven repo without app code changes.

## How to run

1. **Build (artifact only)**: Actions tab, *Build OpenCV Android AAR* or
   *Build ONNX Runtime Android AAR*, Run workflow, keep `release` unchecked.
   Artifacts expire after 90 days.
2. **Publish (GitHub Release)**: same, but check `release`. Each publish
   creates two releases:
   - a stable tag (`opencv-5.0.0`, `onnxruntime-1.26.0`), overwritten on every
     publish. This is the download contract for consumers.
   - a dated history tag (`<stable>-YYYYMMDD`), one per build, for
     traceability.
   Release notes carry the build commit and artifact checksums.

## Configuration

Details like the module list, NDK/CMake pins and expected build times change
often. The workflows and recent run logs are the source of truth:

- `.github/workflows/build-opencv.yml`: OpenCV modules and environment pins
- `.github/workflows/build-ort.yml`: ORT build parameters and environment pins
- `configs/ort/ops.config`: operator whitelist for the reduced ORT build

## Version pinning

- Upstream sources are shallow-cloned at pinned git tags; the resolved commit
  SHA is recorded in the workflow run summary.
- GitHub Actions are pinned by full commit SHA (with `# vX.Y.Z` comments) and
  updated by Dependabot.
- NDK and CMake versions are pinned per workflow; see the workflow file.

## License

This repository is 0BSD. The produced AARs inherit the upstream licenses:
OpenCV is Apache-2.0, ONNX Runtime is MIT.
