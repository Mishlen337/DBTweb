<template>
    <div>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group
          id="input-group-1"
          label="Email address:"
          label-for="input-1"
          description="We'll never share your email with anyone else."
        >
          <b-form-input
            id="input-1"
            v-model="form.email"
            type="email"
            placeholder="Enter email"
            required
          ></b-form-input>
        </b-form-group>
  
        <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.name"
            placeholder="Enter name"
            required
          ></b-form-input>
        </b-form-group>
  
        <b-form-group id="input-group-3" label="Type:" label-for="input-3">
          <b-form-select
            id="input-3"
            v-model="form.report_type"
            :options="report_types"
            required
          ></b-form-select>
        </b-form-group>

        <b-form-group id="input-group-4" label="Text" label-for="input-4">
          <b-form-input
            id="input-4"
            v-model="form.text"
            placeholder="Enter text"
            required
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
      </b-form>
      <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card>
    </div>
  </template>
  
  <script>
    import axios from "axios";
    export default {
      data() {
        return {
          form: {
            email: '',
            name: '',
            report_type: null,
            text: ''
          },
          report_types: [{ text: 'Select One', value: null }, 'Жалоба', 'Пожелание'],
          show: true
        }
      },
      methods: {
        onSubmit(event) {
          event.preventDefault()
          alert(JSON.stringify(this.form))
          axios
          .post("/report", this.form)
          .catch((error) => console.log(error));
        },
        onReset(event) {
          event.preventDefault()
          // Reset our form values
          this.form.email = ''
          this.form.name = ''
          this.form.report_type = null
          this.form.text = ''
          // Trick to reset/clear native browser form validation state
          this.show = false
          this.$nextTick(() => {
            this.show = true
          })
        }
      }
    }
  </script>