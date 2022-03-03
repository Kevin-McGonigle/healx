import AddIcon from "@mui/icons-material/Add"
import CloseIcon from "@mui/icons-material/Close"
import {Box, Card, CardContent, Fab, Grid, Stack, Typography} from "@mui/material"
import * as React from "react"
import {useState} from "react"

import {Document} from "../types"

type Props = {
  document: Document
  onAdd: (document: Document) => void
  onRemove: (document: Document) => void
}

export default function Result({document, onAdd, onRemove}: Props) {
  const [raised, setRaised] = useState(false)
  const [showAddToListButton, setShowAddToListButton] = useState(false)

  const onMouseEnter = () => {
    setRaised(true)
    setShowAddToListButton(true)
  }

  const onMouseLeave = () => {
    setRaised(false)
    setShowAddToListButton(false)
  }

  const authors = () => (
    <Box>
      <Typography
        sx={{color: "text.secondary"}}
        variant={"caption"}
      >
        {document.authors ?? "Unknown Author(s)"}
      </Typography>
    </Box>
  )

  const title = () => (
    <Box>
      <Typography
        variant="h4"
      >
        {document.title ?? "Unknown Title"}
      </Typography>
    </Box>
  )

  const abstract = () => (
    document.abstract ?? (
      <Box>
        <Typography>
          {document.abstract}
        </Typography>
      </Box>
    )
  )

  const addOrRemoveButton = () => (
    showAddToListButton && (
      <Fab
        color={document.reading_list ? "secondary" : "primary"}
        onClick={() => document.reading_list ? onRemove(document) : onAdd(document)}
        size={"small"}
      >
        {document.reading_list ? <CloseIcon /> : <AddIcon />}
      </Fab>
    )
  )

  return (
    <Card
      raised={raised}
    >
      <CardContent>
        <Box
          onMouseEnter={onMouseEnter}
          onMouseLeave={onMouseLeave}
        >
          <Stack>
            <Grid
              container
              spacing={"6"}
            >
              <Grid
                item
                xs
              >
                {authors()}
                {title()}
              </Grid>
              <Grid
                item
                xs={"auto"}
              >
                {addOrRemoveButton()}
              </Grid>
            </Grid>
            {abstract()}
          </Stack>
        </Box>
      </CardContent>
    </Card>
  )
}