import {Box, Stack} from "@mui/material"
import * as React from "react"

import {Document} from "../types"
import Result from "./Result"

type Props = {
  documents: Document[]
  onAdd?: (document: Document) => void
  onRemove: (document: Document) => void
}

export default function ResultsList({
  documents,
  onAdd,
  onRemove,
}: Props) {
  return (
    <Box
      sx={{
        mt: 6,
        width: "100%",
      }}
    >
      <Stack spacing={2}>
        {documents.map(d =>
          <Result
            document={d}
            key={d.id}
            onAdd={onAdd ?? (() => null)}
            onRemove={onRemove}
          />)}
      </Stack>
    </Box>
  )
}