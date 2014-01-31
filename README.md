#Gulp.js Sublime Text 2 & 3 Snippets

This is a [Sublime Text][sublime] package Gulp Sublime Text Snippets
and a plugin "Open browser" Just select the name of plugin and press,
you will be on the plugin docs! 
  
####add in Keys-Bindings-User####

        [
        { "keys": ["ctrl+alt+g"], "command": "open_browser", "args": {"url": "https://npmjs.org/package/%s"}}
        ]

Change at your convenance!


### guv    --->      Gulp.Var.require ####

![guv](http://www.testproject.manolenso.fr/gulp/guv.gif)

### gus    --->      Gulp.Task.src ###

![gus](http://www.testproject.manolenso.fr/gulp/gus.gif)

### guw    --->      Gulp.Watch ###

![guw](http://www.testproject.manolenso.fr/gulp/guw.gif)

### gup    --->      Gulp.pipe ###

![gup](http://www.testproject.manolenso.fr/gulp/gup.gif)

## Installation ##

### Without Package Control ###

This package is not in [wbond's][package_control] repository, so you gotta use Terminal and git to install it. 


#### Mac ####

    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    or
    cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages

#### Linux ###

    cd $HOME/.config/Sublime\ Text\ 2/Packages

#### Windows 7 ####
    cd "%AppData%\Sublime Text 2\Packages\
    or
    cd "%AppData%\Sublime Text 3\Packages\
    
#### Clone repository into packages folder ####
    
    git clone git@github.com:manolenso/gulp-sublime-snippets.git

## Contributing is welcome

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

[sublime]: http://www.sublimetext.com/
[sublime3]: http://www.sublimetext.com/3
[package_control]: http://wbond.net/sublime_packages/package_control
