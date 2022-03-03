import {Box, CircularProgress, Typography} from "@mui/material"
import * as React from "react"
import {useEffect, useState} from "react"

import ResultsList from "../../../components/ResultsList"
import {Document} from "../../../types"

export default function ReadingList() {
  const [documents, setDocuments] = useState<Document[]>([])
  const [loading, setLoading] = useState(false)

  const onRemove = (document: Document) => {
    fetch(
      `http://localhost:8000/reading-list/${document.id}`,
      {
        headers: {"Content-Type": "application/json"},
        method: "delete",
      },
    ).then(() => setDocuments(documents.filter(d => d !== document)), error => console.error(error))
  }

  useEffect(() => {
    setLoading(true)
    fetch("http://localhost:8000/reading-list", {headers: {"Content-Type": "application/json"}})
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
  }, [])

  return (
    <Box
      sx={{
        alignItems: "center",
        display: "flex",
        flexDirection: "column",
        marginTop: 8,
      }}
    >
      <Typography
        gutterBottom
        variant={"h2"}
      >
        Reading List
      </Typography>
      {loading && <CircularProgress />}
      {documents && (
        <ResultsList
          documents={documents}
          onRemove={onRemove}
        />
      )}
    </Box>
  )
}