const baseWebpackConfig = require('./webpack.base.js')
const path = require('path')
const merge = require('webpack-merge')

let webpackConfig = merge(baseWebpackConfig, {
  entry: './script/index.js',
  output: {
    filename: 'dist/demo.js',
    publicPath: '/'
  },
  devServer: {
    compress: true,
    historyApiFallback: true,
    open: true,
    port: 9000
  }
})

module.exports = webpackConfig
