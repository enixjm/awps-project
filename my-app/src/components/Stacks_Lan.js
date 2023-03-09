import * as React from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import Divider from '@mui/material/Divider';
import {Grid, Tabs, Tab, Box } from '@mui/material';

import BarChart from "./BarChart";
import LineChart from "./LineChart";
import PieChart from "./PieChart";
import { UserData } from "./Data";
import { useState } from 'react';

  
export default function ListDividers() {
  const style = {
      width: '100%',
      maxWidth: 180,
      bgcolor: 'background.paper',
      
    };

  const [userData, setUserData] = useState({
      labels: UserData.map((data) => data.year),
      datasets: [
          {
          label: "Users Gained",
          data: UserData.map((data) => data.userGain),
          backgroundColor: [
              "rgba(75,192,192,1)",
              "#ecf0f1",
              "#50AF95",
              "#f3ba2f",
              "#2a71d0",
          ],
          borderColor: "black",
          borderWidth: 2,
          },
      ],
  });

  const [selectedChart, setSelectedChart] = useState(null);

  const handleServerBackEnd = () => {
    setSelectedChart('ServerBackEnd')
  }

  const handleFrontEnd = () => {
    setSelectedChart('FrontEnd')
  }

  const handleWebFullStack = () => {
    setSelectedChart('WebFullStack')
  }

  return (
    <Grid container spacing={2} sx={{
        width: '80%',
    }}>
        <Grid item xs={3}>
        <List 
            sx={style} 
            component="nav" 
            aria-label="mailbox folders"
            >
            <ListItem button onClick={handleServerBackEnd}>
            <ListItemText primary="서버/백엔드" />
            </ListItem>
            <Divider />
            <ListItem button onClick={handleFrontEnd} divider>
            <ListItemText primary="프론트엔드" />
            </ListItem>
            <ListItem button onClick={handleWebFullStack}>
            <ListItemText primary="웹 풀스택" />
            </ListItem>
            <Divider light />
            <ListItem button>
            <ListItemText primary="안드로이드" />
            </ListItem>
            <Divider />
            <ListItem button>
            <ListItemText primary="iOS" />
            </ListItem>
            <Divider />
            <ListItem button>
            <ListItemText primary="머신러닝" />
            </ListItem>
            <Divider />
            <ListItem button>
            <ListItemText primary="인공지능(AI)" />
            </ListItem>
            <Divider />
            <ListItem button>
            <ListItemText primary="데이터 엔지니어링" />
            </ListItem>
            <Divider />
            <ListItem button>
            <ListItemText primary="게임" />
            </ListItem>
        </List>
        </Grid>
          <Grid item xs={9}>
            {selectedChart === 'ServerBackEnd' && <BarChart chartData={userData}/>}
            {selectedChart === 'FrontEnd' && <PieChart chartData={userData}/>}
            {selectedChart === 'WebFullStack' && <LineChart chartData={userData}/>}
          </Grid>
    </Grid>

    );
  }