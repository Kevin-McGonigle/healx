import {Box} from "@mui/material"
import * as React from "react"

import ReadingList from "./components/ReadingList"

export default function ReadingListPage() {
  return (
    <Box
      sx={{
        bgcolor: "background.default",
        color: "text.primary",
      }}
    >
      <ReadingList />
    </Box>
  )
}