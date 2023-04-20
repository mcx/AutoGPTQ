from ._base import *


class LlamaGPTQForCausalLM(BaseGPTQForCausalLM):
    layers_block_name = "model.layers"
    outside_layer_modules = ["model.embed_tokens", "model.norm"]
    inside_layer_modules = [
        ["self_attn.k_proj", "self_attn.v_proj", "self_attn.q_proj"],
        ["self_attn.o_proj"],
        ["mlp.up_proj", "mlp.gate_proj"],
        ["mlp.down_proj"]
    ]

    @staticmethod
    def _resize_attention_mask(attention_mask):
        attention_mask = [each.unsqueeze(1) for each in attention_mask]
        return attention_mask


__all__ = ["LlamaGPTQForCausalLM"]