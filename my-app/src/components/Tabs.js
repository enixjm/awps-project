import { useState } from 'react';
import { Tabs, Tab, Box } from '@mui/material';

import BarChart from "./BarChart";
import LineChart from "./LineChart";
import PieChart from "./PieChart";
import { UserData } from "./Data";

function MyTabs() {
  const [value, setValue] = useState(0);
  const handleChange = (event, newValue) => {
    setValue(newValue);
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

  return (
    <Box sx={{
      width: '80%',
    }}>
      <Tabs value={value} onChange={handleChange} centered>
        <Tab label="BarChart" />
        <Tab label="LineChart" />
        <Tab label="PieChart" />
        <Tab label="Chart" />
      </Tabs>
      {value === 0 && <BarChart chartData={userData}/>}
      {value === 1 && <LineChart chartData={userData}/>}
      {value === 2 && <PieChart chartData={userData}/>}
      {/* {value === 4 && <PieChart chartData={programmersData}/>} */}
    </Box>
  );
}

export default MyTabs;