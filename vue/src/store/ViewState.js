export default {
  state: {
    showFoodModal: false,
    showLoader: false,
    selectedLocation: false,
    selectedLocationURL: ''
  },
  mutations: {
    toggleFoodModal(state) {
      state.showFoodModal = !state.showFoodModal;
    },
    toggleSelectedLocation(state){
      state.selectedLocation = !state.selectedLocation;
    },
    toggleLoader(state) {
      state.showLoader = !state.showLoader;
    }
  }
}