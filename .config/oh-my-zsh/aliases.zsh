# Set-up icons for files/directories in terminal using lsd
alias ls='lsd'
alias l='ls -l'
alias la='ls -a'
alias lla='ls -la'
alias lt='ls --tree'

# Application aliases
alias spotify='spotify_player'
alias matrix='neo-matrix -S 2 -M 1 -d 4 -F -D'
alias ncdu='ncdu --color dark'
alias vim='nvim'

# Set-up FZF key bindings (CTRL R for fuzzy history finder)
source <(fzf --zsh)
