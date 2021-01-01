<template>
  <div class="home__main darken">
    <h1
      class="main__header"
    >Put your link below</h1>

    <vs-input
        v-model="link"
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
          val="60"
      >60 days(Free)
      </vs-radio>
      <vs-radio
          v-model="usageType"
          class="radio"
          val="360"
      >1 Year(0,99$)
      </vs-radio>
      <vs-radio
          v-model="usageType"
          class="radio"
          val="inf"
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
      <p>Input yout custom link: </p>

      <vs-input
          @keydown="checkInput"
          v-model="customLink"
          shadow
          icon-after
          placeholder="Your link..." >
        <template #icon>
          <>
        </template>
        <template #message-warn>
          Max length is 10
        </template>
      </vs-input>

    </div>

    <vs-button
        class="submit__btn"
        @click="createLink"
    >
      Get your truncated link
    </vs-button>

    <vs-dialog
      v-model="getLinkDialog"
    >
      <div class="link__dialog">
        <p>Here is your link, use it</p>

        <div class="link">
          <b>{{ linkDialog.link }}</b>
          <vs-button>
            Copy
          </vs-button>
        </div>
      </div>
    </vs-dialog>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  components: {

  },

  data: () => {
    return {
      usageType: 60,
      link: '',
      useCustomLink: false,
      customLink: 'http:/localhost:8080/',
      getLinkDialog: false,

      linkDialog: {
        link: ''
      }
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
    createLink () {
      if (this.customLink == 'http:/localhost:8080/') {
        axios.post('http://localhost:8000/api/v1/link/',
            {
              initial_link: this.link,
              days: this.usageType,
            })
        .then(response => {
          this.getLinkDialog = true
          this.linkDialog.link = 'http://localhost:8080/' + response.data.truncated_link_uuid
        })
        .catch(error => {

        })
      }
      else {
        axios.post('http://localhost:8000/api/v1/link/',
            {
              initial_link: this.link,
              days: this.usageType,
              truncated_link_uuid: this.customLink.slice(21)
            })
        .then(response => {
          this.getLinkDialog = true
          this.linkDialog.link = 'http://localhost:8080/' + response.data.truncated_link_uuid
        })
        .catch(error => {

        })
      }
    },


  },

  updated() {
  }
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

.link__dialog {
  display: flex;
  flex-direction: column;
}

.link {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

</style>
