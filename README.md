# Stereo Depth Estimation with Parameter Tuning

이 저장소에는 `stereo_depth` 코드를 완성하여 업로드하였습니다. 본 프로젝트에서는 시차(disparity) 맵을 생성하고 깊이(depth) 맵을 추정하는 과정에서 `num_disparities`, `block_size`, `window_size`와 같은 주요 파라미터들을 변경하여 실험을 진행하였습니다. 각 파라미터 값을 조정하면서 결과가 어떻게 달라지는지 시각적으로 확인할 수 있도록 여러 이미지를 첨부하였습니다.

## 실험 설명

- **기준 시차 맵**: 
  - `num_disparities = 96`, `block_size = 15`, `window_size = 6` 설정을 기준으로 생성한 시차 맵을 `Figure 1`에 표시하였습니다. 이 기준 시차 맵을 바탕으로 다른 파라미터 값을 변경하며 실험을 진행하였습니다.

- **`num_disparities` 변경**: 
  - `num_disparities` 값을 기준(96)에서 낮추고(`Figure 2`), 높여(`Figure 3`) 보았습니다. 이를 통해 시차 맵의 범위를 조정하면서 원거리와 근거리 객체의 표현이 어떻게 달라지는지 확인하였습니다.

- **`block_size` 변경**: 
  - `block_size` 값을 기준(15)에서 키운(`Figure 4`) 경우와 줄인(`Figure 5`) 경우를 비교하였습니다. `block_size`는 주변 블록을 얼마나 참조할지를 결정하는 파라미터로, 이 값을 조정하여 디테일과 노이즈 억제 효과를 관찰하였습니다.

- **`window_size` 변경**: 
  - `window_size` 값을 기준(6)에서 늘린(`Figure 6`) 경우와 줄인(`Figure 7`) 경우를 비교하였습니다. `window_size`는 `P1`과 `P2` 패널티 계산에 영향을 주어 시차 맵의 평활화 정도를 조정합니다.

## Depth Map

각 시차 맵에 따라 추정된 깊이 맵은 `depth_figure` 이미지로 제공됩니다. 각 `depth_figure` 이미지는 파라미터 조정에 따른 깊이 맵 변화를 시각적으로 보여주며, 객체 간의 거리 차이를 명확하게 나타내는 데 도움이 됩니다.

---

이와 같은 설명을 통해 시차 맵과 깊이 맵 생성 과정에서 파라미터 변경이 미치는 영향을 이해할 수 있습니다.
