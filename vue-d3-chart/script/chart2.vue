<template lang="pug">
  .line-chart-demo(style="padding-top:200px")
    p.title Chart 2
    line-chart(:width="800", :height="400", :axis="cdata.axis", :line="cdata.line", :trackMouse="true", @action="onLineChartAction")
    table.table.table-bordered.table-hover(style="width:80%; margin:auto")
      thead
        tr
          th No
          th X value
          th Y value
      tbody
        tr(v-for="(item, index) in cdata.line[0].dataset")
          td {{index + 1}}
          td {{item.x}}
          td {{item.y}}
</template>

<script>
import {LineChart} from '../src/index.js'
import axios from 'axios'

export default {
  name: "bar-chart-demo",

  components: {
    LineChart
  },

  data () {
    return {
      cdata: {
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
            dataset: []
          }
        ]
      }
    }
  },
  created () {
    this.getData()
  },
  methods: {
    getData () {
      let _this = this
      axios.get('http://localhost:5000/saved-data-read').then(res => {
        let dataset = []
        res.data.cdata.forEach(i => {
          dataset.push({x: i[0], y: i[1]})
        })
        _this.cdata.line[0].dataset = dataset
      })
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
  th
    text-align: center
</style>



