<template>
  <el-dialog title='Create Alias' :visible.sync='compVisible'>
    <el-form :model='form'>
      <el-form-item label='URL Alias'>
        <el-input id='target-alias' v-model='form.alias' type='text' auto-complete='off' minlength='1' maxlength='20' show-word-limit></el-input>
        <el-alert v-if='!validAlias' title='Error: Input is not a valid alias' type='error' :closable='false' show-icon></el-alert>
      </el-form-item>
      <el-form-item label='Target URL'>
        <el-input id='target-url' v-model='form.target' type='url' auto-complete='off'></el-input>
        <el-alert v-if='!validUrl' title='Error: Input is not a valid URL' type='error' :closable='false' show-icon></el-alert>
      </el-form-item>
    </el-form>

    <span slot='footer' class='dialog-footer'>
      <el-button @click='closeDialog()'>Cancel</el-button>
      <el-button @click='onSubmit()'>Submit</el-button>
    </span>
  </el-dialog>
</template>

<script>
function formAliasIsValid () {
  let tempElem = document.getElementById('target-alias')
  if (tempElem == null) return true
  let tempResult = tempElem.value.length >= 1 && tempElem.value.length <= 20
  return tempResult
}

function formURLIsValid () {
  let tempElem = document.getElementById('target-url')
  if (tempElem == null) return true
  let tempResult = tempElem.validity.valid
  tempResult = tempResult && tempElem.value.length > 0
  return tempResult
}

function closeDialog () {
  this.$emit('update:visible', false)
}

function onSubmit () {
  // TODO: Add logic to send to backend
  let valid = true
  if (!formAliasIsValid()) {
    this.validAlias = false
    valid = false
  } else {
    this.validAlias = true
  }

  if (!formURLIsValid()) {
    this.validUrl = false
    valid = false
  } else {
    this.validUrl = true
  }

  if (valid) {
    this.form.alias = ''
    this.form.target = ''
    this.validUrl = true
    this.validAlias = true
    this.closeDialog()
  }
}

export default {
  name: 'CreateAlias',
  props: {
    visible: Boolean
  },
  data () {
    return {
      formUrlValid: true,
      formAliasValid: true,
      form: {
        alias: '',
        target: ''
      }
    }
  },
  computed: {
    compVisible: {
      get: function () {
        return this.visible
      },
      set: function (newValue) {
        this.closeDialog()
      }
    },
    validUrl: {
      get: function () {
        return this.formUrlValid || formURLIsValid()
      },
      set: function (newValue) {
        this.formUrlValid = newValue
      }
    },
    validAlias: {
      get: function () {
        return this.formAliasValid || formAliasIsValid()
      },
      set: function (newValue) {
        this.formAliasValid = newValue
      }
    }
  },
  methods: {
    onSubmit,
    closeDialog
  }
}
</script>
