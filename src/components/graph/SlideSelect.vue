<template>
  <div class="slider-demo-container">
    <div class="slider-demo-block" ref="slider">
      <div class="slider-track"></div>
      <div
        class="slider-handle"
        v-for="(point, index) in points"
        :key="index"
        :style="{ left: point-2 + '%'}"
        @mousedown="onMouseDown(index)"
      >
        {{ Math.round(point) }}
      </div>
    </div>
  </div>
  
</template>

<script>

export default {
  data() {
    return {
      points: [18, 35, 55], // 初始的三个点位置
      isDragging: false,
      activePointIndex: -1,
    };
  },
  methods: {
    onMouseDown(index) {
      this.isDragging = true;
      this.activePointIndex = index;
    },
    // onTouchStart(index) {
    //   this.isDragging = true;
    //   this.activePointIndex = index;
    // },
    onMouseMove(event) {
      if (!this.isDragging) return;
      const sliderRect = this.$refs.slider.getBoundingClientRect();
      const x = event.pageX - sliderRect.left;
      const percentage = (x / sliderRect.width) * 100;
      this.points[this.activePointIndex] = Math.max(0, Math.min(100, percentage));
    },
    // onTouchMove(event) {
    //   if (!this.isDragging) return;
    //   const sliderRect = this.$refs.slider.getBoundingClientRect();
    //   const x = event.touches[0].pageX - sliderRect.left;
    //   const percentage = (x / sliderRect.width) * 100;
    //   this.points[this.activePointIndex] = Math.max(0, Math.min(100, percentage));
    // },
    onMouseUp() {
      this.isDragging = false;
      this.activePointIndex = -1;
    },
    // onTouchEnd() {
    //   this.isDragging = false;
    //   this.activePointIndex = -1;
    // },
  },
  mounted() {
    document.addEventListener('mousemove', this.onMouseMove);
    document.addEventListener('mouseup', this.onMouseUp);
    // document.addEventListener('touchmove', this.onTouchMove);
    // document.addEventListener('touchend', this.onTouchEnd);
  },
  beforeUnmount() {
    document.removeEventListener('mousemove', this.onMouseMove);
    document.removeEventListener('mouseup', this.onMouseUp);
    // document.removeEventListener('touchmove', this.onTouchMove);
    // document.removeEventListener('touchend', this.onTouchEnd);
  },
};
</script>

<style scoped>
.slider-demo-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 10vh;
  /* background-color: pink; */
}

.slider-demo-block {
  width: 40vw;
  height: 10px;
  /* background-color: #eaeaea; */
  position: relative;
  user-select: none;
  touch-action: none;
  /* margin-left: auto;
  margin-right: auto; */
}

.slider-track {
  /* width: 100%; */
  height: 100%;
  background-color: #f0f0f0;
  border-radius: 5px;
}

.slider-handle {
  position: absolute;
  top: -6px;
  width: 25px;
  height: 25px;
  background-color: #409eff;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 15px;
}

.slider-handle:hover {
  background-color: #66b1ff;
}

.slider-handle:active {
  background-color: #1d6dc2;
}
</style>