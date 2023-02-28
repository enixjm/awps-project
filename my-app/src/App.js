import { useState, useEffect } from "react";

import "./App.css";
import { Button, Box } from '@mui/material';
import { ThemeProvider, createTheme } from '@mui/material/styles';

import ResponsiveAppBar from './components/ResponsiveAppBar';
import MyTabs from './components/Tabs';

// 테마 설정
const theme = createTheme({
  palette: {
    primary: {
      main: '#8a61fb',
    },
    secondary: {
      main: '#2196f3',
    },
  },
});

function App() {


  return (
    <ThemeProvider theme={theme}>
    <div className="App">
    <ResponsiveAppBar/>
    <Box sx={{
      display: 'flex',
      justifyContent: "center",
      margin: '10%',
      border: 'solid',
    }}>
      <MyTabs value={2} />
    </Box>
  </div>
  </ThemeProvider>
  );
}


export default App;

// 메인에다 다 때려박지말고 컴포넌트를 만들어

  // const [programmersData, setProgrammersData] = useState({
  //   labels: [],
  //   datasets: [
  //     {
  //       label: "Users Gained",
  //       data: [],
  //       backgroundColor: [
  //         "rgba(75,192,192,1)",
  //         "#ecf0f1",
  //         "#50AF95",
  //         "#f3ba2f",
  //         "#2a71d0",
  //       ],
  //       borderColor: "black",
  //       borderWidth: 2,
  //     },
  //   ],
  // });

  // useEffect(() => {
  //   const URL =
  //     "https://0h7pzyxz08.execute-api.us-east-2.amazonaws.com/default/get_pay";
  //   fetch(URL, {
  //     headers: {
  //       Accept: "application/json",
  //     },
  //   })
  //     .then((res) => res.json())
  //     .then((data) =>
  //       setProgrammersData({
  //         labels: data.map((data) => data.CompanyName),
  //         datasets: [
  //           {
  //             label: "Users Gained",
  //             data: data.map((data) => data.Pay),
  //             backgroundColor: [
  //               "rgba(75,192,192,1)",
  //               "#ecf0f1",
  //               "#50AF95",
  //               "#f3ba2f",
  //               "#2a71d0",
  //             ],
  //             borderColor: "black",
  //             borderWidth: 1,
  //           },
  //         ],
  //       })
  //     )
  //     .catch((err) => console.error(err));
  // }, []);