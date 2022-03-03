import {Box, Button, Grid, Typography} from "@mui/material"
import * as React from "react"
import {useReducer, useState} from "react"

import ResultsList from "../../components/ResultsList"
import {Document} from "../../types"
import SearchBar from "./components/SearchBar"

export default function SearchPage() {
  const [, forceUpdate] = useReducer(x => x + 1, 0)
  const [documents, setDocuments] = useState<Document[]>([])

  const onAdd = (document: Document) => {
    fetch(
      `http://localhost:8000/reading-list/${document.id}`,
      {
        headers: {"Content-Type": "application/json"},
        method: "post",
      },
    ).then(
      () => {
        document.reading_list = true
        forceUpdate()
      },
      error => console.error(error),
    )
  }

  const onRemove = (document: Document) => {
    fetch(
      `http://localhost:8000/reading-list/${document.id}`,
      {
        headers: {"Content-Type": "application/json"},
        method: "delete",
      },
    ).then(
      () => {
        document.reading_list = false
        forceUpdate()
      },
      error => console.error(error),
    )
  }

  return (
    <Box
      sx={{
        alignItems: "center",
        bgcolor: "background.default",
        color: "text.primary",
        display: "flex",
        flexDirection: "column",
        marginTop: 8,
      }}
    >
      <Typography
        gutterBottom
        variant={"h2"}
      >
        Search
      </Typography>
      <Grid
        container
        spacing={2}
      >
        <Grid
          item
          xs
        >
          <SearchBar setDocuments={setDocuments} />
        </Grid>
        <Grid
          item
          xs={"auto"}
        >
          <Button href={"http://localhost:3000/reading-list"} sx={{height: "100%"}}>
            View Reading List
          </Button>
        </Grid>

      </Grid>
      {documents && (
        <ResultsList
          documents={documents}
          onAdd={onAdd}
          onRemove={onRemove}
        />
      )}
    </Box>
  )
}