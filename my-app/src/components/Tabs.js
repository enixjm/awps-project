import { useState } from 'react';
import { Tabs, Tab, Box } from '@mui/material';

import BarChart from "./BarChart";
import LineChart from "./LineChart";
import PieChart from "./PieChart";
import { UserData } from "./Data";
import { useEffect } from "react";

function MyTabs() {
  const [value, setValue] = useState(0);
  const [subvalue, setSubValue] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const handleSubChange = (event, newSubValue) => {
    setSubValue(newSubValue);
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
      <Tabs
        value={value}
        onChange={handleChange}
        centered
        sx={{bgcolor:'8a61fb'}}
        >
        <Tab label="기술&스택" />
        <Tab label="급여" />
        <Tab label="근무 지역" />
        <Tab label="업무 내용" />
        <Tab label="평균 재직기간" />
      </Tabs>
      {value === 0 && (
        <Box>
          <Tabs
            value={subvalue}
            onChange={handleSubChange}
            centered
            sx={{ bgcolor: "8a61fb" }}
          >
            <Tab label="언어" />
            <Tab label="프레임워크" />
            <Tab label="개발환경"/>
          </Tabs>
          {subvalue === 0 && <BarChart chartData={userData}/>}
          {subvalue === 1 && <LineChart chartData={userData}/>}
          {subvalue === 2 && <PieChart chartData={userData}/>}
        </Box>
      )}
      {value === 1 && <LineChart chartData={userData}/>}
      {value === 2 && <PieChart chartData={userData}/>}
    </Box>
  );
}

export default MyTabs;