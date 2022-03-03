import SearchIcon from "@mui/icons-material/Search"
import {LoadingButton} from "@mui/lab"
import {Box, Grid, TextField} from "@mui/material"
import * as React from "react"
import {Dispatch, SetStateAction, useState} from "react"

import {Document} from "../../../types"

type Props = {
  setDocuments: Dispatch<SetStateAction<Document[]>>
}

export default function SearchBar({setDocuments}: Props) {
  const [loading, setLoading] = useState(false)

  const search = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const data = new FormData(e.currentTarget)
    const query = data.get("query") as string
    setLoading(true)
    fetch(
      `http://localhost:8000/search/${query}?limit=10&method=keyword`,
      {
        headers: {"Content-Type": "application/json"},
      },
    )
      .then(result => result.json())
      .then(
        result => {
          setDocuments(result)
          setLoading(false)
        },
        error => {
          console.error(error)
          setLoading(false)
        },
      )
  }

  return (
    <Box
      component={"form"}
      noValidate
      onSubmit={search}
      sx={{width: "100%"}}
    >
      <Grid
        container
        spacing={2}
      >
        <Grid
          item
          xs
        >
          <TextField
            autoFocus
            fullWidth
            id={"query"}
            label={"Search"}
            name={"query"}
            required
            type={"search"}
          />
        </Grid>
        <Grid
          item
          xs={"auto"}
        >
          <LoadingButton
            endIcon={<SearchIcon />}
            loading={loading}
            loadingPosition={"end"}
            sx={{height: "100%"}}
            type="submit"
            variant={"contained"}
          >
            Search
          </LoadingButton>
        </Grid>
      </Grid>
    </Box>
  )
}