import React from 'react';
import Sidebar from './Sidebar';
import AppBar from '@material-ui/core/AppBar';



class Dashboard extends React.Component {


    render(){
        return(
            <div>
                <AppBar></AppBar>
                <Sidebar></Sidebar>
            </div>
        );
    }
}

export default Dashboard;