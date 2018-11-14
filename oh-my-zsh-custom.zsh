alias wow="git status"
alias such="git"
alias doge="git push"
alias gc="git checkout"
alias gp="git pull"
alias assh="autossh"
alias fport="ss -tlpn | grep"

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
setxkbmap -option caps:escape

# stop zsh autorenaming tmux panes
export DISABLE_AUTO_TITLE="true"

if [ ! -S ~/.ssh/ssh_auth_sock ]; then
    eval `ssh-agent`
    ln -sf "$SSH_AUTH_SOCK" ~/.ssh/ssh_auth_sock
fi
export SSH_AUTH_SOCK=~/.ssh/ssh_auth_sock
ssh-add -l > /dev/null || ssh-add

if [ -z "$TMUX" ]; then
    base_session='playground'
    # Create a new session if it doesn't exist
    tmux has-session -t $base_session || tmux new-session -d -s $base_session
    tmux attach-session -t $base_session
fi
