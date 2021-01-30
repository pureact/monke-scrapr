import React from 'react';
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

const drawerWidth = 240;
const color = "#808080";

const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
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

    const classes = useStyles();
    return (
        <div>
            <Navbar />
            <AppBar position="static" className={classes.appBar}>
                <Toolbar>
                    <Typography variant="h6" className={classes.title}>
                        Create Website Config
                        </Typography>
                </Toolbar>
            </AppBar>
            <Container component="main" maxWidth="xs">
                <CssBaseline />
                <div className={classes.paper}>
                    <AppBar position="static">
                    </AppBar>

                    <form className="classes.form" noValidate>
                        <TextField
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
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="dbName"
                            label="Database Name"
                            name="dbName"
                            autoComplete="dbName"
                            autoFocus
                        />
                        <TextField
                            variant="outlined"
                            margin="normal"
                            required
                            fullWidth
                            id="website"
                            label="Website Link"
                            name="website"
                            autoComplete="website"
                            autoFocus
                        />
                        <TextField
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
                        <Button
                            type="submit"
                            fullWidth
                            variant="contained"
                            color="primary"
                            className={classes.submit}
                        >
                            Create config
                    </Button>
                    </form>
                </div>
                <Copyright />
            </Container>
        </div>
    )
}