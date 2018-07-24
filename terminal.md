1. Install iTerm2 from here [Download Link](https://www.iterm2.com/)

2. Install oh-my-zsh :

 `sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"`
 
3. Install fonts :

 `git clone https://github.com/powerline/fonts.git
 cd fonts
 ./install.sh`

4. Change font on iTerm2 :

 `ITerm2 > Preferences > Profiles > Text > Change Font  ==> Set to “12 Pt Meslo LG DZ for Powerline” font.`

5. Install Powerline Theme

 `git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k`

6. Then edit `~/.zshrc` configuration file and set

 `ZSH_THEME="agnoster"` OR `ZSH_THEME="powerlevel9k/powerlevel9k"`

7. Add Plugins :

 `git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions`
 
 `git clone https://github.com/zsh-users/zsh-completions $ZSH_CUSTOM/plugins/zsh-completions`
 
 `git clone https://github.com/zsh-users/zsh-syntax-highlighting $ZSH_CUSTOM/plugins/zsh-syntax-highlighting`

8. Add the plugin to the list of plugins in `~/.zshrc` configuration file :

 `plugins=(git zsh-autosuggestions zsh-completions zsh-syntax-highlighting)`
 
9. `source ~/.zshrc`
