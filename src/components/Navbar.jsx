import React from 'react';
import Drawer from '@material-ui/core/Drawer';
import Divider from '@material-ui/core/Divider';
import List from '@material-ui/core/List';
import { makeStyles } from '@material-ui/core/styles';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import AddIcon from '@material-ui/icons/Add';
import BuildIcon from '@material-ui/icons/Build';
import HomeIcon from '@material-ui/icons/Home';
import PeopleIcon from '@material-ui/icons/People';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import {Link} from 'react-router-dom';

const drawerWidth = 240;
const useStyles = makeStyles((theme) => ({
    drawer: {
        width: drawerWidth,
        flexShrink: 0,
    },
    drawerPaper: {
        width: drawerWidth,
        background: "#FFF9C2"
    },
    toolbar: theme.mixins.toolbar,
}));

export default function Navbar() {
    const classes = useStyles();

    const [anchorEl, setAnchorEl] = React.useState(null);

    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    return (
        <Drawer
                className={classes.drawer}
                variant="permanent"
                classes={{
                    paper: classes.drawerPaper,
                }}
                anchor="left"
            >
                <div className={classes.toolbar} />
                <Divider />
                <List>
                    <ListItem button component={Link} to="/dashboard">
                        <ListItemIcon><HomeIcon /></ListItemIcon>
                        <ListItemText primary={"Home"}></ListItemText>
                    </ListItem>
                    <ListItem button>
                        <ListItemIcon><BuildIcon /></ListItemIcon>
                        <ListItemText primary={"Scraprs"}></ListItemText>
                    </ListItem>
                    <ListItem button onClick={handleClick}>
                        <ListItemIcon><AddIcon /></ListItemIcon>
                        <ListItemText primary={"Create Scraprs"}></ListItemText>
                    </ListItem>
                    <Menu
                      id="simple-menu"
                      anchorEl={anchorEl}
                      keepMounted
                      open={Boolean(anchorEl)}
                      onClose={handleClose}
                    >
                        <MenuItem component={Link} to="/create/reddit" onClick={handleClose}>Create Reddit Scraper</MenuItem>
                        <MenuItem component={Link} to="/create/twitter" onClick={handleClose}>Create Twitter Scraper</MenuItem>
                        <MenuItem component={Link} to="/create/website" onClick={handleClose}>Create Website Scraper</MenuItem>
                        <MenuItem component={Link} to="/create/praw" onClick={handleClose}>Create PRAW Config</MenuItem>

                    </Menu>
                </List>
                <Divider />
                <List>
                    <ListItem button key={"User"} component={Link} to="/user">
                        <ListItemIcon><PeopleIcon /></ListItemIcon>
                        <ListItemText primary={"User"} />
                    </ListItem>

                </List>
            </Drawer>
    );
}