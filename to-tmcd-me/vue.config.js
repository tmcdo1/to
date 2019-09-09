module.exports = {
    devServer: {
        proxy: {
            '/create-alias': {
                target: 'http://localhost:5000'
            },
            '/alias': {
                target: 'http://localhost:5000'
            },
            '/search': {
                target: 'http://localhost:5000'
            }
        }
    }
}