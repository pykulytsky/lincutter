<template>
  <div class="home__main darken">
    <h1
      class="main__header"
    >Put your link below</h1>

    <vs-input
        shadow
        icon-after
        class="link__input"
        placeholder="Your link..." >

      <template #icon>
        <>
      </template>
    </vs-input>

    <p
      class="p__radio"
    >Choose how long your link will be clickable:</p>
    <div class="radio__section">
      <vs-radio
          v-model="usageType"
          class="radio"
          val="1"
      >60 days(Free)
      </vs-radio>
      <vs-radio
          v-model="usageType"
          class="radio"
          val="2"
      >1 Year(0,99$)
      </vs-radio>
      <vs-radio
          v-model="usageType"
          class="radio"
          val="3"
      >Forever(1,99$)
      </vs-radio>
    </div>

    <vs-checkbox
        class="check__custom__link"
        success
        v-model="useCustomLink">
      Get custom link
    </vs-checkbox>

    <div
        v-if="useCustomLink"
        class="custom__link">
      <p>Lorem ipsum dolor sit amet.</p>

      <vs-input
          @keydown="checkInput"
          v-model="customLink"
          shadow
          icon-after
          placeholder="Your link..." >
        <template #icon>
          <>
        </template>
      </vs-input>

    </div>

    <vs-button
        class="submit__btn"
    >
      Get your truncated link
    </vs-button>
  </div>
</template>

<script>

export default {
  components: {

  },

  data: () => {
    return {
      usageType: 1,
      useCustomLink: false,
      customLink: 'http:/localhost:8080/'
    }
  },
  created() {
    this.$vs.vsTheme.setTheme('darken')
  },
  methods: {
    checkInput (event) {
      if ((event.key === "Backspace" || event.key === "Delete") && this.customLink ==
          'http:/localhost:8080/') {
        return event.preventDefault();
      }
    },

  },
}
</script>

<style scoped>

* {
  color: white;
  font-family: "Vinson", sans-serif;
}

.p__radio {
  margin-top: 25px;
  align-self: self-start;
}

.home__main {
  padding: 50px;
  border-radius: 10%;
  background-color: #1e2023;
  position: absolute;
  left: 50%;
  top: 40%;
  transform: translate(-50%, -50%);

  display: flex;
  flex-direction: column;
  align-items: center;
}

.main__header {
  color: white;
}

.link__input {
  color: white;
  background-color: #18181c;
  border-radius: 10%;
}

.radio__section {
  display: flex;
  margin-bottom: 10px;
  margin-top: 10px;
}

.radio {
  color: white;
  font-size: 14px;
  margin: 0 5px 0 5px;
}

.submit__btn {
  justify-self: flex-end;
  align-self: flex-end;
  margin-top: 25px;
}

.check__custom__link {
  color: white;
  align-self: flex-start;
  margin-top: 20px;
}

.custom__link {
  background-color: #18181c;
  width: 100%;
  padding-left: 15px;
  border-radius: 15px;
  margin-top: 15px;
  display: flex;
  flex-direction: column;
  padding: 10px;
}

</style>
