<template>

</template>

<script>
import axios from 'axios'
export default {

beforeCreate() {
  const loading = this.$vs.loading({
    type: 'corners',
    color: this.color
  })
  const truncatedLink = this.$route.params['link']
  axios.get('http://localhost:8000/api/v1/link/' + truncatedLink)
  .then(response => {
    window.location.replace(response.data.initial_link)
  })

}
}
</script>

<style>
.redirect {
  position: absolute;
  display: flex;
  flex-direction: column;
}
</style>