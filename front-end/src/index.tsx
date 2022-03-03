import {Container} from "@mui/material"
import CssBaseline from "@mui/material/CssBaseline"
import {ThemeProvider} from "@mui/material/styles"
import * as React from "react"
import {render} from "react-dom"
import {BrowserRouter, Route, Routes} from "react-router-dom"

import ReadingListPage from "./routes/reading-list"
import SearchPage from "./routes/search"
import theme from "./theme"

render(
  <ThemeProvider theme={theme}>
    <CssBaseline />
    <Container>
      <BrowserRouter>
        <Routes>
          <Route
            element={<SearchPage />}
            path={"/"}
          />
          <Route
            element={<ReadingListPage />}
            path={"/reading-list"}
          />
        </Routes>
      </BrowserRouter>
    </Container>
  </ThemeProvider>,
  document.querySelector("#root"),
)
