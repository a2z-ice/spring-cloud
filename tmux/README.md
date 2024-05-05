# Fix issue copy paste from/to clipboard ~/.tmux.conf 

# First need to configure and install plugin manager https://github.com/tmux-plugins/tpm
# Then install yank plugin which allow copy from tmux terminal to os clipboard https://github.com/tmux-plugins/tmux-yank?tab=readme-ov-file

```bash
#bind-key S setw synchronize-panes
# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-yank'
set -g status-utf8 on

set paste

set -g mouse on
setw -g mode-keys vi
bind e setw synchronize-panes on
bind E setw synchronize-panes off

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'

```
#  ~/.tmux.conf 
```
# enable to toggle synchronization between panes ctr + b S (control + b and shift s)
bind-key S setw synchronize-panes 
# Enables mouse interaction
set -g mouse on
# Enable copy with selected
setw -g mode-keys vi

```
# cheatsheet of keyboard shortcuts
```
https://tmuxcheatsheet.com/
```

# Install tmux on mac
```
brew install tmux
```
