import * as React from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import Divider from '@mui/material/Divider';
import {Grid, Tabs, Tab, Box } from '@mui/material';

import RadarChart from "./RadarChart";
import BarChart from "./BarChart";
import LineChart from "./LineChart";
import PieChart from "./PieChart";
import { UserData } from "./Data";
import { useState } from 'react';


  
export default function Stacks_Lan() {
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
              "rgba(75,192,192,0.7)",
              "rgba(97,61,248,0.73)",
              "rgba(80,175,149,0.71)",
              "rgba(243,186,47,0.75)",
              "rgba(42,113,208,0.75)",
          ],
          borderColor: "rgba(255, 99, 132, 0.2)",
          borderWidth: 2,
          },
      ],
  });

  const [userData_radar, setUserData_radar] = useState({
      labels: UserData.map((data) => data.year),
      datasets: [
          {
          label: "Users Gained",
          data: UserData.map((data) => data.userGain),
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
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

  const handleAndorid = () => {
    setSelectedChart('Android')
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
            <ListItemText primary="백엔드 개발자" />
            </ListItem>
            <Divider />
            <ListItem button onClick={handleFrontEnd} divider>
            <ListItemText primary="프론트엔드 개발자" />
            </ListItem>
            <ListItem button onClick={handleWebFullStack}>
            <ListItemText primary="웹 풀스택 개발자" />
            </ListItem >
            <Divider light />
            <ListItem button onClick={handleAndorid}>
            <ListItemText primary="데이터베이스" />
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
            {selectedChart === 'Android' && <RadarChart chartData={userData_radar}/>}
          </Grid>
    </Grid>

    );
  }