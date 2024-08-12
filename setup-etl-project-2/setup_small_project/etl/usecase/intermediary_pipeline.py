import asyncio
from typing import Sequence, TypeVar

from setup_small_project.pipeline.step import Step
from setup_small_project.pipeline.usecase.sequential_pipeline import SequentialPipeline

T = TypeVar("T")
V = TypeVar("V")


class IntermediaryPipeline:
    steps: Sequence[Step]
    input_queue: asyncio.Queue
    output_queue: asyncio.Queue
    pipeline: SequentialPipeline

    def __init__(
        self,
        steps: Sequence[Step],
        input_queue: asyncio.Queue,
        output_queue: asyncio.Queue,
    ):
        self.steps = steps
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.pipeline = SequentialPipeline(steps)

    async def execute(self):
        while True:
            input = await self.input_queue.get()
            await self.output_queue.put(self.pipeline.execute(input))
