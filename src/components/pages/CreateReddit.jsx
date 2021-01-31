import React, { useState } from 'react';
import Container from '@material-ui/core/Container';
import { makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import { TextField } from '@material-ui/core';
import Button from '@material-ui/core/Button';
import Copyright from '../Copyright';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Navbar from '../Navbar';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import RadioGroup from '@material-ui/core/RadioGroup';
import Radio from '@material-ui/core/Radio';
import axios from 'axios';

const drawerWidth = 240;
const color = "#FF5700";

const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
    },
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    content: {
        flexGrow: 1,
        height: '100vh',
        overflow: 'auto',
    },
    appBarSpacer: theme.mixins.toolbar,
    appBar: {
        width: `calc(100% - ${drawerWidth}px)`,
        marginLeft: drawerWidth,
        background: color
    },
    form: {
        width: '100%',
        marginTop: theme.spacing(1),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
    title: {
        align: 'left'
    },
}));

export default function CreateReddit() {

    const [configName, setConfigName] = useState("");
    const [subreddit, setSubreddit] = useState("");
    const [numPosts, setNumPosts] = useState(0);
    const [sorting, setSorting] = useState("");
    const [keywords, setKeywords] = useState([]);
    const [trackedUsers, setTrackedUsers] = useState([]);

    const handleSubmit = () =>{
        console.log(configName,subreddit,numPosts,sorting,keywords,trackedUsers);
        console.log("test");
        console.log(configName,subreddit,numPosts,sorting,keywords.split(),trackedUsers.split());
        
        setKeywords(keywords.split(" "));
        setTrackedUsers(trackedUsers.split(" "));

        axios.post("localhost:5000/create/createConfig",configName,subreddit,numPosts,sorting,keywords,trackedUsers);
    }

    const classes = useStyles();
    return (
        <div className={classes.root}>
            <CssBaseline />

            <AppBar position="fixed" className={classes.appBar}>
                <Toolbar>
                    <Typography variant="h6" noWrap>
                        Create Reddit Config yep
                    </Typography>
                </Toolbar>
            </AppBar>
            <Navbar />
            <main className={classes.content}>
                <div className={classes.appBarSpacer} />
                <Container maxWidth="xs" className={classes.container}>
                <form className={classes.form} noValidate>
                        <TextField
                            value={configName}
                            onInput={ e=>setConfigName(e.target.value)}
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="configName"
                            label="Config Name"
                            name="configName"
                            autoComplete="configName"
                            autoFocus
                        />
                        <TextField
                            value={subreddit}
                            onInput={ e=>setSubreddit(e.target.value)}
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="subreddit"
                            label="Subreddit"
                            name="subreddit"
                            autoComplete="subreddit"
                            autoFocus
                        />
                        <TextField
                            value={numPosts}
                            onInput={ e=>setNumPosts(e.target.value)}
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="numPost"
                            label="Number of posts to search"
                            name="numPost"
                            autoComplete="Number of posts to search"
                            autoFocus
                        />
                        <TextField
                            value={trackedUsers}
                            onInput={ e=>setTrackedUsers(e.target.value)}
                            variant="outlined"
                            margin="normal"
                            fullWidth
                            id="trackedUsers"
                            label="Tracked Users"
                            name="trackedUsers"
                            autoComplete="trackedUsers"
                            autoFocus
                        />
                        <TextField
                            value={keywords}
                            onInput={ e=>setKeywords(e.target.value)}
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="keywords"
                            label="Keywords"
                            name="keywords"
                            autoComplete="keywords"
                            autoFocus
                        />

                        <RadioGroup aria-label="gender" name="gender1" value={sorting} onChange={ e=>setSorting(e.target.value)}>
                            <FormControlLabel value="Hot" control={<Radio />} label="Hot" />
                            <FormControlLabel value="New" control={<Radio />} label="New" />
                            <FormControlLabel value="Rising" control={<Radio />} label="Rising" />
                            <FormControlLabel value="Controversial" control={<Radio />} label="Controversial" />
                            <FormControlLabel value="Top" control={<Radio />} label="Top"></FormControlLabel>
                        </RadioGroup>

                        <Button
                            onClick={handleSubmit}
                            type="submit"
                            fullWidth
                            variant="contained"
                            color="primary"
                            className={classes.submit}
                        >
                            Create config
                    </Button>
                    </form>
                <Copyright />
                </Container>
                </main>
        </div>
    )
}