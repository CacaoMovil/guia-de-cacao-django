module.exports = function(grunt) {
grunt.initConfig({

    // connect: {
    //     server: {
    //         options: {
    //             port: 4567,
    //             protocol: 'http',
    //             hostname: '0.0.0.0',
    //             base: '.',
    //             open: true,
    //             debug: true,
    //             keepalive: false
    //         }
    //     }
    // },

    less: {
        development: {
            options: {
                compress: true,
                yuicompress: true,
                cleancss: false,
                optimization: 2
            },
            files: {
                "css/custom.css": "less/custom.less",
                "css/uielement.min.css": "less/uielement.less",
                "css/layout.min.css": "less/layout.less",
                "css/colors-guias.min.css": "less/colors-guias.less"
            }
        }
    },

    autoprefixer: {
        single_file: {
            options: {
                browsers: ['last 3 version', 'ie > 8']
            },
            src: 'css/custom.css',
            dest: 'css/custom.css'
        }
    },

    watch: {
        styles: {
            files: ['less/*.less', 'less/*/*.less'],
            tasks: ['buildless'],
            options: {
                nospawn: true,
                livereload: true
            }
        },
        html: {
            files: ['*.html'],
            options: {
                nospawn: true,
                livereload: true
            }
        }
    }
});

    //grunt.loadNpmTasks('grunt-contrib-connect');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-autoprefixer');
    grunt.loadNpmTasks('grunt-contrib-watch');

    //grunt.registerTask('default', ['connect','watch']);
    grunt.registerTask('default', ['watch']);
    grunt.registerTask('buildless', ['less', 'autoprefixer']);
};
