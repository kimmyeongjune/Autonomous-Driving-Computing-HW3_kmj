# Stereo Depth Estimation with Parameter Tuning

stereo_depth.py에 코드를 완성하여 업로드하였습니다. 시차(disparity) 맵을 생성하고 깊이(depth) 맵을 추정하는 과정에서 num_disparities, block_size, window_size와 같은 주요 파라미터들을 변경하여 실험을 진행하였습니다. 각 파라미터 값을 조정하면서 결과가 어떻게 달라지는지 시각적으로 확인할 수 있도록 여러 이미지를 첨부하였습니다.

## 실험 설명

- **기준 시차 맵**: 
  - num_disparities = 96, block_size = 15, window_size = 6 설정을 기준으로 생성한 시차 맵을 Figure 1에 표시하였습니다. 이 기준 시차 맵을 바탕으로 다른 파라미터 값을 변경하며 실험을 진행하였습니다.

- **num_disparities 변경**: 
  - num_disparities 값을 기준(96)에서 줄인(Figure 2) 경우와 높인(Figure 3) 경우를 비교하였습니다.

- **block_size 변경**: 
  - block_size 값을 기준(15)에서 키운(Figure 4) 경우와 줄인(Figure 5) 경우를 비교하였습니다. 

- **window_size 변경**: 
  - window_size 값을 기준(6)에서 늘린(Figure 6) 경우와 줄인(Figure 7) 경우를 비교하였습니다. 

## Depth Map

각 시차 맵에 따라 추정된 깊이 맵은 depth_figure 이미지로 제공됩니다. 각 depth_figure 이미지는 파라미터 조정에 따른 깊이 맵 변화를 시각적으로 보여주며, 객체 간의 거리 차이를 명확하게 나타내는 데 도움이 됩니다.

---

