<template lang="pug">
  .line-chart-demo(style="padding-top:200px")
    p.title Chart 1
    line-chart(:width="800", :height="400", :axis="cdata.axis", :line="cdata.line", :trackMouse="true", @action="onLineChartAction")
    div.content
      button.btn.btn-primary(@click="saveData") Save Data 
</template>

<script>
import {LineChart} from '../src/index.js'
import axios from 'axios'
const cdata = {
  axis: {
    x: [0, 600],
    xDiv: 10,
    y: [0, 150],
    yDiv: 10,
    xLabel: "Y",
    yLabel: "X",
  },
  line: [
    {
      label: 'Gold',
      color: 'green',
      dataset: [],
    }
  ]
}

export default {
  name: "line-chart-demo",

  components: {
    LineChart
  },

  data () {
    return {
      cdata
    }
  },
  computed: {
  },
  created () {
    this.ajaxData()
  },
  mounted () {
    this.updateCdata()
  },
  methods: {
    updateCdata () {
      setInterval(this.ajaxData, 10000)
    },

    ajaxData () {
      let _this = this
      axios.get('http://localhost:5000/random-data-read',{headers: {"Access-Control-Allow-Origin": "*"}}).then(res => {
        let dataset = []
        let xdata = 0
        res.data.cdata.forEach((i,j) => {
          if(j==0) {
            dataset.push({x:0,y:i[1]})
          }
          else {
            xdata += i[0]
            dataset.push({x:xdata,y:i[1]})
          }
        })
        _this.cdata.line[0].dataset = dataset
      })
    },

    saveData () {
      let data = []
      this.cdata.line[0].dataset.filter(i => {
        data.push([i.x,i.y])
      })
      axios.post('http://localhost:5000/data-save',{data: data}).then(res => {})
    },

    onLineChartAction (params) {
      const {origin, act, payload} = params

      switch (act) {
        case origin.ACT_CLICK_LINE:
          alert(`Line ${payload} clicked`)
          break
        case origin.ACT_CLICK_DOT:
          alert(`Dot ${payload.pointIndex} in line ${payload.lineIndex} clicked`)
          break
        default:
          break
      }
    },
  }
}
</script>

<style lang="stylus" scoped>
  .line-chart-demo
    text-align: center
  .title
    text-align: center
    font-size: 32px
    font-weight: bold
</style>



